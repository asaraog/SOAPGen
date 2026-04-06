## Generating SOAP notes from audio using Microsoft Azure
**Abstract**

SOAPgen is a healthcare AI and LLM project focused on converting recorded clinical conversations into structured SOAP notes: Subjective, Objective, Assessment, and Plan. The goal is to reduce manual documentation time for clinicians and make patient records easier to organize, review, and share.

The pipeline uses Microsoft Azure services for speech processing and downstream text handling, followed by an LLM to organize the content into the standard SOAP format. Audio is first transcribed, then the resulting text is cleaned and structured into a concise clinical summary.

Beyond automation, the project highlights how cloud-based AI tools can support real-world medical documentation tasks. SOAPgen sits at the intersection of natural language processing, speech technology, and data engineering, with an emphasis on building practical tooling for healthcare settings.

Future directions: After a Business Associate Agreement (BAA) is signed with OneDrive for Business, the watcher function can be removed with Power Automate.

To run locally, download or git clone this project:
```
git clone https://github.com/asaraog/soapgen.git
cd soapgen
python3 watcher.py
```
Record and add audio file to local environment for testing. See my [website](https://saraogee.com/SOAPgen/). 
