import os, sys, glob, subprocess

report = sorted(glob.glob(os.environ['REPORT_PATH']))
if not report:
    sys.exit(f"Report file does not exist: {os.environ['REPORT_PATH']}")

recipients = [r.strip() for r in os.environ['REPORT_RECIPIENTS'].split(',') if r.strip()]
body = os.environ.get('BODY', 'Please find the attached scan report.')
attach = [x for r in report for x in ("-a", r)]

cmd = ["mail", "-s", os.environ.get('SUBJECT'), "-r", os.environ['SENDER'], *attach, *recipients]

subprocess.run(cmd, input=body, universal_newlines=True, check=True)
print(f"Email sent: {report}")