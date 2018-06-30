from insta_meter import InstaMeter

im = InstaMeter(username='al_kricha')
res = im.analyze_profile()
im.print_account_statistic()
im.print_top_liked()
im.print_top_commented()
im.print_top_viewed()
