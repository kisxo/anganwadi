from uuid import uuid4
from fastapi import HTTPException
import base64

def save_image(image_str: str, image_group: str, center_id: int) -> str:
    """
    image_group = ``students`` or ``staffs``
    Specify whose image to save and determine correct file route
    """
    if not image_str:
        raise HTTPException(status_code=400, detail="Image not found !")
    try:
        # Format: center_id + '-' + uuid
        unique_image_id = f"{center_id}-{uuid4()}"
        with open(f"media/images/{image_group}/{unique_image_id}.jpg", "bw") as image_file:
            contents = base64.b64decode(image_str)
            image_file.write(contents)
        return unique_image_id
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid image file !")