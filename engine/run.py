"""One command runs the whole pipeline and leaves a dated log behind."""
import os
import subprocess
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    day = datetime.utcnow().strftime("%Y-%m-%d")
    logdir = os.path.join(ROOT, "logs")
    if not os.path.isdir(logdir):
        os.makedirs(logdir)
    logpath = os.path.join(logdir, "run-%s.log" % day)

    with open(logpath, "a") as log:
        log.write("\n===== run %sZ =====\n" % datetime.utcnow().isoformat())
        for step in ("ingest.py", "score.py", "verify.py", "synthesize.py"):
            header = "\n--- %s ---" % step
            print(header)
            log.write(header + "\n")
            log.flush()
            proc = subprocess.Popen(
                [sys.executable, os.path.join(HERE, step)],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for raw_line in proc.stdout:
                line = raw_line.decode("utf-8", "replace")
                sys.stdout.write(line)
                log.write(line)
            proc.wait()
            if proc.returncode != 0 and step == "ingest.py":
                log.write("ingest produced nothing; stopping.\n")
                print("ingest produced nothing; stopping.")
                return 0
    print("\nlog -> %s" % logpath)
    return 0


if __name__ == "__main__":
    sys.exit(main())
