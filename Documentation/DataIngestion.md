# Data Ingestion

- Launch Azure Data Factory
- In ADF, we need to create an Integration Run time service (Computation Engine) to start working with ADF
  - If On Prem DB, then we need to use Self Hosted.
  - If on Cloud, then we can use Default Integration Run time

![image](https://github.com/Subramanian-Thiagarajan/ADE_Project_1/assets/96657323/84f53fdd-10be-48ce-8261-013c1f6aadf2)

- Setup Github or Azure DevOps to track the changes and for version control

- Integration Run Time - default
  ![image](https://github.com/Subramanian-Thiagarajan/ADE_Project_1/assets/96657323/dae38b35-c777-414c-b086-3ba170749cb3)

- Add a pipeline
  ![image](https://github.com/Subramanian-Thiagarajan/ADE_Project_1/assets/96657323/1ea2af56-f8d5-410c-9a4e-bac02e93d735)

- Create Linked Service - Azure Key Vault, Source SQL Database
  ![image](https://github.com/Subramanian-Thiagarajan/ADE_Project_1/assets/96657323/723178ca-b730-4297-9aa9-23208084afd8)
