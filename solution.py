# %% [markdown]
# # **Image processing using OpenCV**
# ## Detecting the red and blue objects within the given frame and making a line between them

# %% [markdown]
# ## Import Libraries

# %%
import cv2
import numpy as np

# %% [markdown]
# ### Masking red and blue

# %%
def PreProcessing(frame):
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper boundaries for red color
    lower_red1 = np.array([0, 90, 90])
    upper_red1 = np.array([8, 255, 255])
    lower_red2 = np.array([172, 90, 90])
    upper_red2 = np.array([180, 255, 255])

    # Define the lower and upper boundaries for blue color
    lower_blue = np.array([90, 90, 90])
    upper_blue = np.array([130, 255, 255])
    
    # Create masks for red and blue colors
    red_mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    red_mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Combine the red and blue masks
    combined_mask = cv2.bitwise_or(red_mask1, red_mask2)
    
    # Perform morphological operations to refine the mask (optional)
    kernel = np.ones((5, 5), np.uint8)
    combined_mask = cv2.erode(combined_mask, kernel, iterations=1)
    combined_mask = cv2.dilate(combined_mask, kernel, iterations=1)
    blue_mask = cv2.erode(blue_mask, kernel, iterations=1)
    blue_mask = cv2.dilate(blue_mask, kernel, iterations=1)
    
    # Find contours for the reference colors
    red_reference_contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    blue_reference_contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    return (red_reference_contours,blue_reference_contours)

# %% [markdown]
# ### making rectangle and centerpoint around contours:-

# %%
def markingRectangles(contours,frame):
    color = (0, 255, 0)  # Green color for rectangles
    min_contour_area = 100
    cont = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(cont)
    if area > min_contour_area:
        # Draw rectangle around the largest red contour
            #detecting rectangle
            x, y, w, h = cv2.boundingRect(cont)
            w+=x
            h+=y
            #Making rectangle
            cv2.rectangle(frame, (x, y), (w,h), color, 2)
            p = int((x + w) / 2)
            q = int((y + h) / 2)
            cv2.circle(frame, (p, q), radius=3, color=(0,0,0), thickness=-1)
            return (p,q)
    else: return (-1,-1)
    

# %% [markdown]
# ### Make a line between the Rectangle

# %%
def gettingLine(red_contour, blue_contour, frame):
    # min_contour_area = 200
    if len(red_contour) > 0 and len(blue_contour) > 0:
        
        p1,q1=markingRectangles(red_contour,frame)
        p2,q2=markingRectangles(blue_contour,frame)
        if p1>=0 and q1>=0 and p2>=0 and q2>=0:
            cv2.line(frame, (p1,q1), (p2, q2), (0, 255, 0), thickness=3)

            ax=(p1 + p2) / 2
            ay=(q1 + q2) / 2

            cv2.circle(frame, (int(ax), int(ay)), radius=2, color=(0, 0, 0), thickness=-1)
        
    cv2.imshow('hehe', frame)
    


# %% [markdown]
# ### Execution Phase

# %%
cap = cv2.VideoCapture(0)

while(True):
    
    ret, frame = cap.read()
    #flipping cause it shows mirror image otherwise    
    frame = cv2.flip(frame,1)

    # combined_window = np.hstack([gray_flip])
    # min_contour_area=200
    
    contours=0
    
    #Function area...
    
    red,blue=PreProcessing(frame=frame)
    # contours=MaskOperations(combined_mask)
    gettingLine(frame=frame,red_contour=red,blue_contour=blue)
    # print(contours)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # break

# When everything done, release the capture

cap.release()
cv2.destroyAllWindows()




