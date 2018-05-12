import shangyin.storage as storage
import shangyin.server as server

# Connect database
db = storage.Storage()
db.setup()

# Start up the statistics server
srun = server.ServerRunner()
srun.assign_db(db)
srun.start()