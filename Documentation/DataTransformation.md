# Data Transformation

1. Launch Databricks Workspace
   
   ![image](https://github.com/Subramanian-Thiagarajan/ADE_Project_1/assets/96657323/9202cb6f-a92a-4a5e-9133-22c244ab3983)

2. In the compute tab, create a cluster as shown in the screenshot below

   ![image](https://github.com/Subramanian-Thiagarajan/ADE_Project_1/assets/96657323/59dbe11c-9f37-482b-9bdc-303558ecb606)

- Mark the check box to access ADLS from DBW with the user logged into DBW. Make sure to give the user access to Storage Blob contributor in ADLS as follows

  ![image](https://github.com/Subramanian-Thiagarajan/ADE_Project_1/assets/96657323/ed41cd98-006a-4cad-8121-1a6c590c3051)

3. Go to workspace, and create a notebook to mount adls in DBW
   
5. Create Silver and Gold ADLS and apply the transformations as shown in the dbw-code-folder
