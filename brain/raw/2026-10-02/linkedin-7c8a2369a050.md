---
author: Matthias van der Vlies
fetched_at: '2026-10-02T09:09:52.297375Z'
id: 7c8a2369a050
lane: lead
published: ''
source: linkedin
title: 'Something I''ve found that works really well when using LLMs for protocol
  work: give them something independent to check'
url: https://www.linkedin.com/posts/mvdvlies_wireshark-3gpp-telecom-activity-7511701452017344512-KgeH
---

Something I've found that works really well when using LLMs for protocol work: give them something independent to check their output against.

A lot of what I work with is binary protocols: Diameter, S1AP, GTP, Sigtran, etc. The starting point is always an RFC or a 3GPP/ETSI spec.

A common mistake is having the LLM implement both the encoder and decoder and then using a round-trip test as proof that it works. If both have the same misunderstanding of the spec, the test passes.

For protocols supported by Wireshark, there's a very simple additional check: emit the bytes and let Wireshark decode them.

Spec → implementation → bytes → Wireshark

I basically instruct the LLM to use the tshark command on the CLI to decode PCAPs that I either capture or construct.

This works remarkably well. Wrong lengths, malformed messages, missing IEs, incorrectly encoded values, you get an independent view of what you actually put on the wire.

It doesn't solve everything. Wireshark validates what you send; it doesn't prove your decoder correctly handles everything a peer might send.

For that, existing test vectors are extremely useful. Milenage is a good example: the spec provides known inputs and expected outputs. Depending on the protocol, the same role can be filled by a reference implementation, known-good PCAPs, or interoperability tests against another stack.

None of this is new. I used to do the same validation manually, walking through hex dumps with the spec tables next to me. And yes also checking on the wire and check the pcaps visually.

What's changed with LLMs is the speed of the loop:

implement → encode → validate → fix → repeat

The validation techniques we already had become even more useful when the implementation itself gets much faster.

Same technique, different 'operator', and honestly mostly better results in less time.

#Wireshark #3GPP #Telecom #ProtocolEngineering #LLM
