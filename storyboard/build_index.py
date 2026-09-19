#!/usr/bin/env python3
"""Generate storyboard/panels.md from urls.tsv plus the beat table below."""
import os

BEATS = [
 (1,"0:01-0:06",'"What the hell are you waiting for? 6 hours of speeches?"',"Tension","Dutch angle",
  ["Wide full body, arms thrown up","Medium-wide, palms spread","Medium, mid-shout","Medium close, head tipped back"]),
 (2,"0:06-0:09",'"What the hell is going on?"',"Tension","Dutch angle",
  ["Medium, looking back over the shoulder","Medium close, frowning back","Close-up, brow furrowed","Wide, hand on hip, turned back"]),
 (3,"0:09-0:15",'"Hey, where are you going?" / "You escaped too?" / "Yeah"',"Neutral","Eye-level",
  ["Wide two-shot, Gasuka on the bench","Medium on Gasuka, hand raised","Medium on Muhire, mild surprise","Medium two-shot, Muhire walking over"]),
 (4,"0:15-0:21",'"The uncle took the mic again?" / "I\'m not going back"',"Neutral","Eye-level",
  ["Medium two-shot, thumb jerked at the hall","Close on Gasuka, knowing smile","Medium on Muhire, arms folded","Wide two-shot, Muhire sits down"]),
 (5,"0:21-0:28",'"Gasuka, groom\'s side." / "Muhire. Bride\'s side." / "So we\'re enemies tonight"',"Conflict","Over-the-shoulder",
  ["Over Gasuka onto Muhire, hand extended","Reverse over Muhire onto Gasuka","Over Gasuka, the handshake","Reverse over Muhire, half smile"]),
 (6,"0:28-0:38",'"Only if the food runs out." / "Uncle, you look stressed."',"Intimacy","Close-up",
  ["Close on Muhire, teasing grin","Close on Gasuka, pinching his nose","Close on Muhire, leaning in","Extreme close on Muhire's eyes"]),
 (7,"0:38-0:48",'"Grass." / "Like the lawn?" / "No uncle. The special grass."',"Intimacy","Close-up",
  ["Close on Muhire, fingers pinched","Close on Gasuka, blank","Close on Gasuka, glancing down","Close on Muhire, correcting him"]),
 (8,"0:49-0:58",'"I\'m not a smoker, I\'m an artist." / "These hands?"',"Power","Low angle",
  ["Medium, hand on his chest","Close from below, proud","Medium, both palms presented","Wide full body, arms spread"]),
 (9,"0:58-1:08",'"Picasso, baby. They call me the King of Leaves."',"Power","Low angle",
  ["Medium, thumbs at his chest","Close from below, wide grin","Wide, standing on the bench","Medium-wide, arms overhead"]),
 (10,"1:08-1:18",'"I\'ve met kings. They all talk like that, before they fall."',"Tension","Dutch angle",
  ["Medium on Gasuka, level stare","Close on Gasuka, cold","Medium two-shot, grin faltering","Close on Muhire, smile frozen"]),
 (11,"1:18-1:26",'"Fall? Me? Never. Not once."',"Power","Low angle",
  ["Medium, waving it away","Close from below, scoffing","Medium, finger raised","Wide full body, swaggering"]),
 (12,"1:26-1:37",'"Nobody ever caught you?" / "Police are too busy with traffic."',"Conflict","Over-the-shoulder",
  ["Over Muhire onto Gasuka, asking","Reverse onto Muhire, dismissive","Over Muhire onto Gasuka, probing","Reverse onto Muhire, laughing"]),
 (13,"1:37-1:47",'"My father knows people." / "Everybody\'s father knows people."',"Conflict","Over-the-shoulder",
  ["Over Gasuka onto Muhire, smug finger","Reverse onto Gasuka, unimpressed","Over Gasuka onto Muhire, shrugging","Reverse onto Gasuka, sceptical"]),
 (14,"1:48-1:58",'"I can spot a cop a mile away. The walk. The shoes."',"Tension","Dutch angle",
  ["Medium, counting on his fingers","Close, miming a stern face","Medium two-shot, gesturing down","Close on Gasuka, carefully blank"]),
 (15,"1:58-2:07",'"Police always wear shoes like-"',"Tension","Dutch angle",
  ["Low medium, the shoes sliding under the bench","Close on Gasuka, tight neutral","Wide two-shot, feet withdrawing","Close on Muhire, oblivious"]),
 (16,"2:08-2:22",'"Groom\'s side. Bride\'s side. Tonight we\'re family."',"Intimacy","Close-up",
  ["Close on Muhire, hand on his heart","Close on Gasuka, small nod","Tight close, hand into the shirt pocket","Close on Muhire, leaning right in"]),
 (17,"2:22-2:34",'"Wedding special. Tonight I show you real art."',"Intimacy","Close-up",
  ["Close on Muhire, the paper twist raised","Close on Gasuka, eyes dropping","Close on Gasuka, eyes lifting","Close on Muhire, delighted"]),
 (18,"2:35-2:45",'"No more parties. Inspector Gasuka."',"Power","Low angle",
  ["Medium, rising with the badge out","Tight low on the badge wallet","Close from below, hard and calm","Wide full body, feet planted"]),
 (19,"2:45-2:57",'"Police? At a wedding?" / "Police get invited too."',"Weakness","High angle",
  ["Medium looking down, shoulders drawn in","Close on the upturned face, panic","Medium two-shot, standing over him","Wide, small in the frame"]),
 (20,"2:57-3:10",'"Hands behind your back, King of Leaves."',"Weakness","High angle",
  ["Medium, hands going behind the back","Close, head lowered, protesting","Medium-wide, a hand on the shoulder","Wide from above, wrists together"]),
 (21,"3:10-3:21",'"Call it a wedding gift. Nobody has to know."',"Intimacy","Close-up",
  ["Tight close, the note between two hands","Close on Muhire, pleading","Close on Gasuka, eyes down, refusing","Extreme close on the folded note"]),
 (22,"3:21-3:33",'"Put it away. And that\'s two charges."',"Power","Low angle",
  ["Medium, pushing the money back","Tight low, the cuffs closing","Close from below, implacable","Wide two-shot, cuffed beside him"]),
 (23,"3:33-3:44",'Muhire raging / "Who is it?" / "Afande." / "Papa."',"Tension","Dutch angle",
  ["Medium, twisting against the cuffs","Close, contorted with rage","Medium two-shot, both heads snapping round","Close on Gasuka, recognition"]),
 (24,"3:44-3:51",'Papa arrives. "Inspector. What\'s happening here?"',"Awe","Worm's-eye",
  ["Wide from the ground, Papa towering","Medium, looking down past camera","Close from far below, glasses catching light","Wide three-shot, the others tiny"]),
 (25,"3:51-4:02",'"I see no grass. I see a boy at his cousin\'s wedding."',"Power","Low angle",
  ["Medium on Gasuka, at attention","Medium on Papa, hand raised","Close on Papa, absolute authority","Wide two-shot, Papa dominating"]),
 (26,"4:02-4:11",'"Remove the cuffs, inspector." / "Yes, Afande."',"Weakness","High angle",
  ["Medium on Gasuka, head lowered","Tight, hands unlocking the cuffs","Close on Gasuka, defeated","Medium two-shot, Muhire rubbing his wrists"]),
 (27,"4:11-4:20",'"My father knows people." / "I refused the money and still lost."',"Isolation","Wide / bird's-eye",
  ["Bird's-eye, alone beside the bench","Extreme wide, lone figure, huge empty space","Extreme wide, the others walking away","Bird's-eye, seated alone with the open cuffs"]),
]

urls = {}
with open(os.path.join(os.path.dirname(__file__), "urls.tsv")) as fh:
    for line in fh:
        line = line.strip()
        if not line:
            continue
        key, url = line.split("\t", 1)
        urls[key] = url

out = ["# Panel Index", "",
       "108 panels, four per beat. The camera angle is fixed per beat by the",
       "emotion rule in `storyboard.md`; only the shot size changes inside a beat.",
       "All panels are anchored to the same character sheet.", "",
       "## Character anchor sheet", ""]
if "anchor" in urls:
    out.append(f"![Character anchor sheet]({urls['anchor']})")
    out.append("")

missing = []
for num, time, line, emotion, angle, shots in BEATS:
    out.append(f"## Beat {num:02d} — {time} — {emotion} — {angle}")
    out.append("")
    out.append(f"{line}")
    out.append("")
    for i, shot in enumerate(shots, start=1):
        key = f"{num}{i:02d}"
        url = urls.get(key)
        if url:
            out.append(f"**{num:02d}.{i} {shot}**")
            out.append("")
            out.append(f"![Beat {num:02d} panel {i}]({url})")
            out.append("")
        else:
            missing.append(key)
            out.append(f"**{num:02d}.{i} {shot}** — panel pending")
            out.append("")

with open(os.path.join(os.path.dirname(__file__), "panels.md"), "w") as fh:
    fh.write("\n".join(out).rstrip() + "\n")

print(f"panels written: {sum(1 for _ in BEATS) * 4 - len(missing)}/108")
if missing:
    print("missing:", ", ".join(missing))
