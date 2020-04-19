from argparse import ArgumentParser
from mail_manager import MailManager
from utils.templates import get_template,render_context

parser=ArgumentParser(prog="sendmail")
parser.add_argument("type",type=str,choices=['View','Message'])
parser.add_argument('-id','--user_id',type=int)
parser.add_argument('-email','--email',type=str)
parser.add_argument('-sub','--subject',type=str)

args=parser.parse_args()

if args.type=="View":
     print(MailManager().get_user_data(user_id=args.user_id,email=args.email))
elif args.type=="Message":
     print(MailManager().message_user(user_id=args.user_id,email=args.email,subject=args.subject))