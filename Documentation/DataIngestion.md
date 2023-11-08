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

- Create Linked Service - Azure Key Vault, Source SQL Database, ADLS Gen 2
  
  ![image](https://github.com/Subramanian-Thiagarajan/ADE_Project_1/assets/96657323/723178ca-b730-4297-9aa9-23208084afd8)

  ![image](https://github.com/Subramanian-Thiagarajan/ADE_Project_1/assets/96657323/ae1c42c2-c68a-4b9d-b1b9-16c2a806bfb1)

- Create Datasets to reference the actual data in sql db

  ![image](https://github.com/Subramanian-Thiagarajan/ADE_Project_1/assets/96657323/3072f7a0-5425-4373-af2b-027d9a4f4698)

- Create a dataset to reference to the bronze sink in adls gen 2

  ![image](https://github.com/Subramanian-Thiagarajan/ADE_Project_1/assets/96657323/4e8a21c6-163f-4ff0-996e-9b46c2dca954)

- Create a Pipeline to copy data from Source to Bronze Sink

  ![image](https://github.com/Subramanian-Thiagarajan/ADE_Project_1/assets/96657323/21c3b0a1-ab83-483a-b89c-f236d6be0ad7)
