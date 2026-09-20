# Research Factory Data Contract

यह directory research agents के बीच canonical claim/evidence format निर्धारित करती है।

## Processing rule

हर महत्वपूर्ण कथन को पहले **claim record** में बदला जाए। इसके बाद agent:

1. claim को classify करे;
2. definitions स्पष्ट करे;
3. उपलब्ध primary/secondary sources खोजे;
4. evidence records जोड़े;
5. आवश्यकता होने पर mathematical/computational formulation करे;
6. counterexamples खोजे;
7. independent या automated verification करे;
8. status तय करे;
9. provenance सुरक्षित करे।

## "सिद्ध" का अर्थ

Factory में **PROVED / SUPPORTED** केवल उसी अर्थ में इस्तेमाल होगा जो record की evidence और verification वास्तव में support करती है।

- logical derivation → premises से conclusion तक validity
- mathematical result → stated assumptions के भीतर derivation
- computational result → reproducible code/test के भीतर result
- empirical claim → उपलब्ध evidence और verification के अनुसार
- historical claim → traceable historical sources के अनुसार
- philosophical proposition → framework proposition के रूप में, जब तक स्वतंत्र empirical evidence अलग से उपलब्ध न हो

## तुलनात्मक engine

तुलना करते समय प्रत्येक पक्ष के लिए समान fields रखे जाएँ:

**परिभाषा → स्रोत → evidence → formulation → strengths/limitations → counterexamples → verification → conclusion**

किसी पक्ष को केवल अधिक साहित्य, अधिक लोकप्रियता या AI-generated confidence के आधार पर सत्य घोषित नहीं किया जाएगा।

## Quantum / infinity / ultra-mega formulation

इन शब्दों को decorative certainty के रूप में नहीं इस्तेमाल किया जाएगा। यदि कोई प्रश्न quantum, infinity, formal logic, probability, statistics या किसी अन्य technical method मांगता है, तो agent पहले उसका operational mathematical meaning तय करेगा। जहाँ कोई well-defined method लागू नहीं होता, result में **NOT_APPLICABLE** या **NOT_VERIFIED** दर्ज होगा।

## Missing evidence

Missing source, unavailable private material या failed retrieval को fabricated text से नहीं भरना है।

