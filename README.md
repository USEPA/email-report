# Email Security Report Action
This GitHub Action emails a container scan report as an attachment. It is designed to deliver the result of an automated container scan on a schedule after each scan. 



## Description
The action takes the path to a report file that already exist on the runner (typically produced after a scan) attaches report and mauls it to recipients.



## Input
| Name         |   Description            | Required | Default |
|--------------|--------------------------|----------|---------|
|report_path   | Path to the report file  |   Yes    |     -
|recipients    | Passed as variables      |   Yes    |     -
|sender        | Passed as variable       |   Yes    |     -



## Output 
This action does not produce any direct outputs. it emails the specific report file as an attachment. 


## Usage 
```yaml
name: email 

on:
  schedule:
    - cron: '00 9 * * 1,4'
    
env:
    REPORT_DIR: /data/watchtower/*/container-results/filepath

jobs:
    send-email:
        runs-on: "th878"
        steps:
        - name: Email latest report
          uses: USEPA/email-report@main
          with:
                report_path: ${{ env.REPORT_DIR }}/filename.html
                recipients: ${{ vars.REPORT_RECIPIENTS }}
                sender: ${{ vars.REPORT_SENDER }}
                subject: "Filename Scan Report"
                body: |
                    Hello,

                    Please find attached the Filename scan report.

                    Best regards.

