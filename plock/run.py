import sh


plone = sh.Command('bin/plone')
run = plone('fg', _bg=True)

print("Plone is now running on http://localhost:8080. CTRL-C to quit.")
run.wait()
