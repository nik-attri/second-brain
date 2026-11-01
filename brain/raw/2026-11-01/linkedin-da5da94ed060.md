---
author: Abolfazl Khanmohammadi
fetched_at: '2026-11-01T09:53:43.090170Z'
id: da5da94ed060
lane: lead
published: ''
source: linkedin
title: '​We all know that satisfying (or annoying) blue squiggly line in VS Code telling
  us to add const to our widgets.

  ​Most d'
url: https://www.linkedin.com/posts/abolfazl-khanmohammadi_part-3-const-activity-7522577010896863232-6IDD
---

​We all know that satisfying (or annoying) blue squiggly line in VS Code telling us to add const to our widgets.
​Most devs just hit Cmd + . to make the linter happy and move on.
​But if you saw yesterday’s post on the Element Tree, what const actually does under the hood is kind of wild.
​When a parent widget rebuilds, Flutter calls Element.updateChild() on every child. Normally, the Element has to allocate a new Widget object in memory, run Widget.canUpdate(), and then call build() on that child.
​Unless you used const.
​Look at the actual Flutter SDK source code on Slide 3:
Right at the top of updateChild(), before Flutter does any diffing, it runs one ultra-fast check:
​if (child.widget == newWidget) return child;
​Because a const widget is canonicalized at compile time, Dart reuses the exact same object at the exact same memory address on every single build.
​When Flutter hits a const widget during a rebuild:
​Zero RAM allocation: No new object is created, which means zero Garbage Collection (GC) pressure.
​Instant short-circuit: child.widget == newWidget evaluates to true in a single CPU cycle.
​Subtree freeze: Flutter immediately returns the existing Element and skips rebuilding that widget and all of its children.
​This is also the real reason why senior Flutter devs tell you to stop using helper methods like Widget _buildHeader() and extract a StatelessWidget class instead. A function call can never be const—meaning its contents get rebuilt and re-evaluated every single time. A custom StatelessWidget with a const constructor gets skipped completely.
​📌 Part 3 of 30 in my Flutter Under the Hood series. Tomorrow in Part 4, we’ll tackle one of the most misunderstood topics in Flutter: Keys (ValueKey, ObjectKey, and GlobalKey)—and why your stateful lists break without them.
​Be honest: do you have "source.fixAll": "explicit" turned on in VS Code to auto-insert const on save, or do you still add them manually? 👇
​#flutter #dart #mobiledevelopment #softwareengineering #appdevelopment #cleancode
