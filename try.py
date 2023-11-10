import pickledb

db = pickledb.load('try.db', True)

if not db.get('counter'):
    db.set('counter', 1)
    db.dump()
    
def next_id():
    counter = db.get('counter')
    db.set('counter', counter+1)
    db.dump()
    return counter

def set_info(title, text):
    db.set(str(next_id), {"title" : title, "text" : text})
    db.dump(    )
    

print(db.get("id1"))




