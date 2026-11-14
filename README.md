# The world on Friday 13 November 2026

A photographic newspaper infographic summing up 13 November 2026 in one
image: 28 stories, verified against reporting from BBC, Reuters and Al
Jazeera. The program delivers the bundled image to `/output/entry.png`.

## The image

- Format: JPEG bytes under the filename `entry.png` (1024 x 1024, under
  1 MiB), as the competition allows.
- Layout: masthead, one feature story, ten illustrated stories, and a
  digest of seventeen more under "ALSO ON FRIDAY 13 NOVEMBER".

## The 28 stories

Feature:

1. US Senate summons Nvidia chief Huang and Commerce Secretary Lutnick
   to testify.

Illustrated:

2. Zelensky meets US envoys as Europe joins talks.
3. Ukrainian drone hits Russian warship in the Gulf of Finland.
4. Iran says it struck a US radar site in Bahrain.
5. FBI: North Korean hackers stole $400m in crypto via fake video calls.
6. US reports a record 483,200 deportations in 2026.
7. FAA orders a nationwide ground stop after a communications outage.
8. Turkiye and Qatar sign a mutual defence pact.
9. South Sudan's Kiir dissolves the government.
10. Gaza storms flood camps; 106,000 affected (UNICEF).
11. Kane breaks the England caps record with his 126th cap.

Digest:

12. Salah breaks Egypt's scoring record in a 5-0 win.
13. Man Utd appoint Pochettino as manager.
14. UN extends the Abyei peacekeeping mandate to 2027.
15. Pakistan: 74 militants killed near the Afghan border.
16. Six killed as a building collapses near Nairobi.
17. Tens of thousands join Poland's nationalist march.
18. UK police investigate Walliams allegations.
19. Tanzania opposition leader Lissu jailed.
20. Niger says the army regained control after a mutiny attempt.
21. Somalia security forces seize the top court.
22. NGOs demand a probe into a Guinea mass grave.
23. Cameroon attackers kill an officer and kidnap teachers.
24. UK curbs DRC visas; deals with Angola and Namibia.
25. 7,400+ migrants reach the Canary Islands in 10 days.
26. Pope Leo XIV welcomed by 1.5m in Chiclayo, Peru.
27. Nigeria clears 62 Ebola contacts; none fell ill.
28. Gaza baby dies of cold; WHO warns of infections.

## How it works

`main.py` (standard library only, no network) copies the bundled
`entry.png` to `/output/entry.png`, first checking the JPEG magic bytes,
the 1 MiB size limit, and the 1024 x 1024 dimensions.
