from argparse import ArgumentParser
from mail_manager import MailManager
from utils.templates import get_template,render_context


parser=ArgumentParser(prog="sendmail")
parser.add_argument("type",type=str,choices=['View','Message','MessageAll','ViewAll','MessageRange','ViewRange'])
parser.add_argument('-id','--user_id',type=int)
parser.add_argument('-email','--email',type=str)

args=parser.parse_args()

if args.type=="View":
     print(list(MailManager().get_user_data(user_id=args.user_id,email=args.email).items()))

elif args.type=="Message":
     s=input("Enter Subject ")
     print(MailManager().message_user(user_id=args.user_id,email=args.email,subject=s))

elif args.type=="ViewAll":
     print(MailManager().get_all_users())

elif args.type=="MessageAll":
     s=input("Enter Subject ")
     print(MailManager().message_all_users(subject=s))

elif args.type=="ViewRange":
     start,end=map(int,input("Enter start and end id no ").split())
     print(MailManager().get_within_range(start=start,end=end))

elif args.type=="MessageRange":
     s=input("Enter Subject ")
     start,end=map(int,input("Enter start and end id no ").split())
     print(MailManager().message_within_range(subject=s,start=start,end=end))
