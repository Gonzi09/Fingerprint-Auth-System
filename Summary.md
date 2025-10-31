# SUMMARY TEMPLATE

Answer all the questions. Please put your answers _after_ the italicized instructions.

## Parameter Selection Rationale  
_Explain how you decided on your default values for the maximum number of tries and the error threshold. Why did you choose these particular thresholds? How do they balance security, usability, and fairness?_  


I set the default maximum number of tries to 3 because it provides users a fair balance between security and convenience allowing for minor human error, such as finger misplacement, without compromising protection.The error threshold (match threshold) was set to 0.9, meaning fingerprints must be at least 90% similar to be considered a match. This value helps minimize false positiveswhile still allowing for small variations caused by pressure or sensor noise.


## Stakeholder-value Matrix
_Please put a stakeholder-value matrix for fingerprint-based login systems. Include at least five stakeholders and at least three values, one of which should be Privacy._


| Stakeholder          | Privacy                    | Security           | Usability   |

| **End Users**             | Ensures biometric data is stored and used safely         | Prevents unauthorized access to their personal accounts     | Provides quick, convenient logins without passwords                 |
| **System Administrators** | Maintains compliance and limits data visibility          | Monitors breaches and enforces lockouts                     | Simplifies management of authentication logs                 |
| **Developers**            | Designs systems to minimize data exposure                | Implements accurate matching and error handling             | Delivers smooth user experience and low false rejections             |
| **Organizations**         | Reduces liability from data leaks                        | Protects sensitive business assets                          | Boosts employee and customer satisfaction                 |
| **Regulators**            | Upholds data-protection standards (e.g., GDPR)     

---

## Citations

### Who did you work with and how?  
_Discussing the assignment with people not on your team is fine as long as you don't share code._  
_Please include any people or other sources who helped you, and any students whom you helped._  
_For each source, make sure to include how they helped you (or how you helped them)._  

* _“I discussed the authentication loop design with classmate Alice Smith and clarified how to break out of the while loop.”_  
* _“I showed Bob Lee my test plan for mocking input and he suggested using `side_effect` in `unittest.mock.patch`.”_  
* _If you did not talk to anybody about the assignment, please state that._

i did not talk to anybody
---

### What resources did you use?  
_Please give specific URLs (not “Stack Overflow” or “Google”) and state which ones were particularly helpful._  

* _https://docs.python.org/3/library/unittest.mock.html – for guidance on `patch` and `side_effect`._  
* _If you did not consult any external resources, please state that._

---

## Logistics

### Did you successfully implement everything that was requested?  
_Answer “Yes”, or state here which parts did not work or which tests did not pass._  

yes 
### How long did the assignment take?  
_Rather than giving a range, if you are unsure, give the average of the range._  

1 day aprox with multiple pauses
---

## Reflections  
_Give **one or more paragraphs** reflecting on your experience with the assignment, including answers to all of these questions:_  
* What was the most difficult part of the assignment?  
* What was the most rewarding part of the assignment?  
* What did you learn doing the assignment?  
* Constructive and actionable suggestions for improving assignments, office hours, and lecture are always welcome.  

The most challenging part of the assignment was getting the fingerprint comparison to handle different file formats correctly without running into index errors. Debugging the equality function helped me better understand string handling and 2D list manipulation.The most rewarding part was seeing all the tests pass once everything aligned with the autograder’s expectations.
I learned how to create class methods, use properties effectively, and design custom exceptions that make error handling clearer.
For future improvements, clearer examples of how the fingerprint data files are structured and expected test behaviors would make the setup faster.
---
