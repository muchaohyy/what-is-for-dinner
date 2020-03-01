# What is for dinner

### Python environment
```bash
# 1. Install or update python to version 3.8
# 2. cd to the directory where requirements.txt is located
# 3. Optional: activate your virtualenv
# 4. Run the following command to install required python packages
pip3 install -r requirements.txt
```

### How to run unit test
```bash
# 1. cd to the directory where Makefile is located
# 2. Run the following command to kick off unit test
make unittest
```

### How to run live process
```bash
# 1. cd to the directory where Makefile is located
# 2. Run the following command to kick off live run
make find_dinner
```

### Further improvement
```bash
# Take AWS platform as example
# 1. Redesign the whole process in serverless architecture
# 2. Use lambda to run the logic in python code
# 3. Take input as json event and return the result in json
# 4. Use API gateway to expose the lambda as API
# 5. Use S3 to host fridge information
# 6. Involve data process, if file of fridge information needs to be processed, such as data cleansing, validation, transformation, etc.
# 7. Think about saving file of fridge information in parquet format rather than csv, which will bring less space cost, faster query time, column-oriented design and metadata layer.
# 8. Use Athena to build external table on top of file in s3 to SQL query if data auditing is needed.
# 9. Serverless framework can be used as development frame to work with version control and CICD if it is neccessary.
# 10. More design improvement can be discussed in further interview.
```