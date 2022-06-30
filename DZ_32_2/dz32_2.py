from jinja2 import FileSystemLoader, Environment

file_loader = FileSystemLoader('temp')
env = Environment(loader=file_loader)

tm = env.get_template('footer.html')
msg = tm.render()

print(msg)