class Task:
    def __init__(self,userid, name, description,time,status):
        self.userid = userid
        self.name = name
        self.description = description
        self.time = time
        self.status = status
        

    def to_dict(self):
        return {
            "userid": self.userid,
            "name": self.name,
            "description": self.description,
            "time": self.time,
            "status": self.status
        }

    def __str__(self):
        return f"{self.name} - {self.description} - {self.time}"

    
