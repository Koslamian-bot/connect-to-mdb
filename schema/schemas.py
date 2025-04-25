def individual_serial(sample) -> dict:
    return{
        "id" : str(sample["_id"]),
        "name" : sample["name"],
        "audio_id" : sample["audio_id"],
        "desc" : sample["desc"]
    }

def list_all(samples) -> list:
    return[individual_serial(sample) for sample in samples]