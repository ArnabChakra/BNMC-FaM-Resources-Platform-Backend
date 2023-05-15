# BNMC-FaM-Resources-Platform-Backend

<h1 align="center">YouBe-Healthy 👋</h1>

## Description

🔍 YouBe-Healthy specializes in providing various health related resources that aim to improve the well-being of our members. Among our initiatives is the implementation of the Medically Tailored Meals program, which was developed by the NYS DOH. Through our application of this program as an \"In Lieu of Services\" offering, we strive to reduce inpatient and emergency visits for members with specific conditions and ultimately enhance their health outcomes. Additionally, we have launched the FoodFirst program, which addresses food deserts by providing free grocery delivery to members' homes in identified areas.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Tests](#tests)
- [Questions](#questions)

## Installation

💾 Step 1: Download codebase and other files from current repo<br/>
💾 Step 2: Go to this URL, download and install Python : https://www.python.org/downloads/<br/>
💾 Step 3: Go to this URL, download and install Anaconda : https://www.anaconda.com/download<br/>
💾 Step 4: Open Anaconda prompt and using the requirements.txt file provided create Conda environment using following command : _conda create --name <env> --file <this file>_<br/>
💾 Step 5: Activate new environment : _conda activate <env>_<br/>
💾 Step 6: Open windows command prompt and enter ipconfig -> capture IPv4 Address under **Wireless LAN adapter Wi-Fi**<br/>
💾 Step 7: Open run.py file and update _host_ with above captured IP Address<br/>
💾 Step 8: On earlier opened Anaconda prompt execute command : python run.py<br/>

**NOTE :** This will bring up the backend system. Similar procedure needs to be followed for frontend as well to bring it up. Make sure both of them are running under same WiFi connection.

## Data Update

If you want to upload new/updated data to database follow below steps:
  * Run database_updater.exe 
  * Update data in Master_data_v4.csv
  * Upload above csv, db_cred_uri.txt and private.pem via tool and wait for tool to execute update
  
## Usage

💻 Web application to provide food as medicine resources within a specific area or location

## Contributing

👪 Arnab Chakravarty and Upendra Kumar

## Tests

✏️ No

## Questions

✋ contact chakravartyarnab93@gmail.com or shawkumarupendra@outlook.com<br />
<br />
:octocat: Find me on GitHub: [ArnabChakra](https://github.com/ArnabChakra)<br />
<br />
✉️ Email me with any questions: chakravartyarnab93@gmail.com<br /><br />
