# निष्पक्ष समझ — बहु-आयामी विश्लेषण प्रोटोकॉल

किसी शब्द, अनुभव, दृश्य, कथन, सूत्र, घटना या दावे को केवल एक अर्थ में सीमित न करना। तथ्य, अनुभव, व्याख्या और अनुमान अलग रखना।

## विश्लेषण आयाम
- शब्द/भाषिक — spelling, grammar, literal meaning, usage.
- अर्थ/semantic — प्रयुक्त अर्थ, ambiguity और alternative meanings.
- संदर्भ — वाक्य, घटना, समय, व्यक्ति और परिस्थिति.
- multi-angle — जहाँ संभव हो कम-से-कम तीन स्वतंत्र व्याख्याएँ.
- visual — आकार, स्थिति, प्रकाश, रंग और pattern; observation को कारण/पहचान से अलग रखना.
- sensory — sight, sound, touch, smell, taste; direct observation बनाम interpretation.
- perceptual — lighting, occlusion, attention और observer effects.
- finger-vein/biometric — raw image या sensor data होने पर pattern analysis; identity inference के लिए independent validation.
- eye/ocular — उपलब्ध visual data का वर्णन; स्वतः health diagnosis या identity inference नहीं.
- temporal — chronology, timestamps और before/after evidence.
- spatial — स्थान, दिशा, दूरी और relative position.
- causal — correlation और causation अलग; mechanisms और alternatives.
- mathematical — symbols, domains, units, dimensions और consistency.
- computational — code, reproducibility, tests और deterministic checks.
- empirical — measurable predictions, datasets, experiments और replication.
- countercase — claim को कमजोर करने वाला evidence.
- epistemic — हमें यह कैसे पता है; source quality और uncertainty.
- ontological — claim किस प्रकार की entity/process के बारे में है.
- operational — abstract term को measurable definition में बदलना.
- ethical/privacy — biometric, health और personal data में minimum necessary handling.
- accessibility — क्या दूसरा observer वही observation कर सकता है.
- reproducibility — independent person/system वही result दोहरा सकता है.
- security/provenance — original source, hash, timestamp और transformation trail.
- negative evidence — indexed evidence न मिलना स्वतः false नहीं है.
- alternative explanation — causal/extraordinary claim में plausible alternatives.

## निष्पक्षता के नियम
- Observation ≠ interpretation ≠ hypothesis ≠ proof.
- Source-backed ≠ independently verified.
- Automated test PASS ≠ scientific truth.
- Image pattern ≠ identity.
- Correlation ≠ causation.
- Absence of indexed evidence ≠ proof of absence.
- Extraordinary claims के लिए stronger independent evidence आवश्यक.
- अस्पष्ट data को UNKNOWN रखें; अनुमान से खाली जगह न भरें.

## Finger-vein sensing उदाहरण
raw image/sensor → image quality → visible pattern → segmentation → feature extraction → algorithm → reference dataset → false-accept/false-reject metrics → independent replication → privacy/security review.

## रिकॉर्ड
claim → definitions → observations → multi-angle interpretations → evidence → countercases → formulation/test → independent verification → limitations → status
