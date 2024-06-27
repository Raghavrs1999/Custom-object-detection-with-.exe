import cv2
from gui_buttons import Buttons

# Initialize the Buttons class, which will be used to create and manage buttons on the GUI
button = Buttons()

button.add_button("person", 20, 20)
button.add_button("cell phone", 20, 100)
button.add_button("cat", 20, 180)
button.add_button("dog", 20, 260)
button.add_button("chair", 20, 340)

# Get the colors associated with each button
colors = button.colors

# Load the YOLOv4-tiny model using OpenCV's DNN module
net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(640, 640), scale=1/255)  # Set the input parameters for the model

# Load the class list from a file
classes = []
with open("dnn_model/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)

print("Objects list")
print(classes)  # Print the list of classes

# Initialize the camera
cap = cv2.VideoCapture(4)  # Open camera device 4
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # Set the frame width to 1280
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # Set the frame height to 720

# Define a callback function for mouse clicks
def click_button(event, x, y, flags, params):
    global button_person
    if event == cv2.EVENT_LBUTTONDOWN:  # If the left mouse button is clicked
        button.button_click(x, y)  # Call the button_click function with the x and y coordinates

# Create a window and set the mouse callback function
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", click_button)

while True:
    # Get a frame from the camera
    ret, frame = cap.read()

    # Get the list of active buttons
    active_buttons = button.active_buttons_list()
    #print("Active buttons", active_buttons)

    # Perform object detection using the YOLOv4-tiny model
    (class_ids, scores, bboxes) = model.detect(frame, confThreshold=0.3, nmsThreshold=.4)
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y, w, h) = bbox
        class_name = classes[class_id]
        color = colors[class_id]

        # If the detected class is in the list of active buttons, draw a bounding box and label
        if class_name in active_buttons:
            cv2.putText(frame, class_name, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 3, color, 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 3)

    # Display the buttons on the frame
    button.display_buttons(frame)

    # Display the frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27 or key == ord("q"):  # If the Esc or q key is pressed, break out of the loop
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()