# संपूर्ण संतुष्टि की निरंतरता — Operational Runbook

निरंतरता का अर्थ हर कार्य को एक साथ पूरा घोषित करना नहीं है। अर्थ है कि प्रत्येक चरण स्पष्ट स्थिति में हो, परिणाम दर्ज हो और अगला उपयोगी कदम चुना जाए।

## दैनिक कार्य-चक्र
1. देखें — वर्तमान वास्तविक स्थिति पढ़ें।
2. समझें — source, claim, evidence और implementation अलग करें।
3. चुनें — सबसे छोटा उपयोगी अगला कार्य तय करें।
4. करें — सीमित परिवर्तन करें।
5. जाँचें — syntax, links, tests और status देखें।
6. दर्ज करें — commit/change और परिणाम रिकॉर्ड करें।
7. सीखें — failure या feedback से अगला सुधार चुनें।
8. दोहराएँ — केवल प्रमाणित स्थिति को आगे बढ़ाएँ।

## Fail-closed
- Missing file को complete न मानें।
- Workflow run को scientific verification न मानें।
- Generated page को independent evidence न मानें।
- अनुमानित income, sale, job या user outcome को realized outcome न मानें।
- High-impact निर्णय को बिना accountable human review के automate न करें।

## Completion signals
IMPLEMENTED → TESTED → DEPLOYED → LIVE → VERIFIED

इन signals को एक-दूसरे का पर्याय न माना जाए। Independent verification अलग gate है।

## Public navigation check
The continuity surface should link only to files that exist on the same release branch. When a referenced file is missing, treat the release as not complete and repair the link or restore the file before declaring the module LIVE.

## Release discipline
Before merging a continuity change: validate JSON contracts, run available tests, inspect the public entry points, and record any unavailable CI result explicitly. Never infer PASS from the absence of a reported failure.
