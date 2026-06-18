import os, sys, subprocess

report = os.environ['REPORT_PATH']
if not os.path.isfile(report):
    sys.exit(f"Report file does not exist: {report}")

recipients = [r.strip() for r in os.environ['REPORT_RECIPIENTS'].split(',') if r.strip()]
body = os.environ.get('BODY', 'Please find the attached scan report.')

cmd = ["mail", "-s", os.environ.get('SUBJECT'), "-r", os.environ['SENDER'], "-a", report, *recipients]

subprocess.run(cmd, input=body, universal_newlines=True, check=True)
print(f"Email sent: {report}")