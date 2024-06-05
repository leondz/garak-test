import garak
import garak.detectors.mitigation

with open("misinfo_mitigations.txt", "r") as mitigation_file:
    mitigation_messages = mitigation_file.read().strip().split("\n")

mitigation_messages_lower = [m.lower() for m in mitigation_messages]

d = garak.detectors.mitigation.MitigationBypass()
mitigation_strings_lower = [s.lower() for s in d.substrings]

# 1 = mitigation is here.
# i.e. opposite scoring scheme from mitigationbypass, sorry
scores = [1 if any(m in msg for m in mitigation_strings_lower) else 0 for msg in mitigation_messages_lower]

score = sum(scores)/len(scores)

print(">> score", score)
failed_items = [mitigation_messages[i][:120] for i, v in enumerate(scores) if v == 0]
print("\n".join(failed_items))