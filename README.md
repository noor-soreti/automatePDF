# Overview
This web application was built with Python using the Flask framework and leverages the ``camelot py`` python library. It address common issues by users who want to extract tabular data from pdf files. I built this web app to practice implementing a custom solution where I could review my Docker knowledge and gain more hands-on experience with different cloud environments and tools, in this case, Google Cloud Run. 

I decided to use Flask as my backend framework. It is a lightweight and flexible framework making it suitable for my web app. My backend consists of a single HTTP route that handles both ``GET`` AND ``POST`` request. Once the initial web page is displayed, the user has to specify the output file format (xlsx, csv, json) and the names and number of columns. When a user uploads and submits a form, it triggers a ``POST`` request that calls ``camelot-py`` function to read and extract tabular data. After the file contents are sent to the client in the format specified by the user.

Google Cloud Run is a fully managed platform that lets you run code in a serverless environment making it ideal for applications that don't require high computational resources.
