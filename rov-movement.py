import numpy as np
import cv2


#Class for vehicle movement
class Rov():
    def __init__(self):
        print("Araç aktif!")

    def yaw_left(self):
        print("Dairenin merkezine yönelmek için yaw ekseninde sola dön.")
        
    def yaw_right(self):
        print("Dairenin merkezine yönelmek için yaw ekseninde sağa dön.")
    
    def pitch_down(self):
        print("Dairenin merkezine yönelmek için pitch ekseninde asagi dön.")
    
    def pitch_up(self):
        print("Dairenin merkezine yönelmek için pitch ekseninde yukari dön.")

    def roll_left(self):
        print("Dairenin merkezine yönelmek için roll ekseninde sola dön.")

    def roll_right(self):
        print("Dairenin merkezine yönelmek için roll ekseninde sağa dön.")

    def forward(self):
        print("İleri git.")

    def yaw_circular_right(self):
        print("Çemberin tam önüne gelmek için yaw ekseninde sağa dön ve ileri git. (Sola doğru dairesel hareket)")

    def yaw_circular_left(self):
        print("Çemberin tam önüne gelmek için yaw ekseninde sola dön ve ileri git. (Sağa doğru dairesel hareket)")

    def desired_direction(self):
        print("Araç çemberden geçmek için istenilen doğrultuda. Dümdüz ilerle!")

    def stop(self):
        print("Çemberi geçtin! Dur!")

#finds the center of the circle
def circle_center(x,y,w,h):
        x_axis = (x + x + w) / 2
        y_axis = (y + y + h) / 2
        return (x_axis, y_axis)
        

#Decision function of the vehicles movement
def movement_decider(x,y,w,h,width,height,turn_right_indicator,passing_count,rectangle_count):
    (center_X,center_Y) = circle_center(x,y,w,h)

    if h < 80:
        if rectangle_count < 1 or h < 50:
            rov.ileri()
            return 0
        
        else:
            if center_X > (width/2) + 40 and center_Y > (height/2) + 40:
                rov.pitch_down()
                rov.yaw_right()
                rov.forward() 
                return 0
                
            elif center_X > (width/2) + 40 and center_Y < (height/2) - 40:
                rov.pitch_up()
                rov.yaw_right()
                rov.forward()
                return 0
                
            elif center_X < (width/2) - 40 and center_Y > (height/2) + 40:
                rov.pitch_down()
                rov.yaw_left()
                rov.forward()
                return 0
                   
            elif center_X < (width/2) - 40 and center_Y < (height/2) - 40:
                rov.pitch_up()
                rov.yaw_left()
                rov.forward()
                return 0
            
            elif center_X < (width/2) - 65 and (height/2) - 65 < center_Y < (height/2) + 65:
                rov.yaw_left()
                rov.forward()
                return 0

            elif center_X > (width/2) + 65 and (height/2) - 65 < center_Y < (height/2) + 65:
                rov.yaw_right()
                rov.forward()
                return 0
            
            elif (width/2) - 65 < center_X < (width/2) + 65 and center_Y < (height/2) - 65:
                rov.pitch_up()
                rov.forward()
                return 0
            
            elif (width/2) - 65 < center_X < (width/2) + 65 and center_Y > (height/2) + 65:
                rov.pitch_down()
                rov.forward()
                return 0

            else:
                rov.forward()         
                return 0      
            
    if 80 < h < 310:
        if rectangle_count < 1:
            rov.forward()
            return 0
        
        else:
            if h - 10 < w < h + 10:
                #araç çemberin tam ortasında    
                rov.desired_direction()
                return 0
                
            elif center_X > (width/2) + 35 and center_Y > (height/2) + 35:
                rov.pitch_down()
                rov.yaw_right()
                rov.forward() 
                return 0
                
            elif center_X > (width/2) + 35 and center_Y < (height/2) - 35:
                rov.pitch_up()
                rov.yaw_right()
                rov.forward()
                return 0
                
            elif center_X < (width/2) - 35 and center_Y > (height/2) + 35:
                rov.pitch_down()
                rov.yaw_left()
                rov.forward()
                return 0
        
            elif center_X < (width/2) - 35 and center_Y < (height/2) - 35:
                rov.pitch_up()
                rov.yaw_left()
                rov.forward()
                return 0

            elif center_X < (width/2) - 65 and (height/2) - 65 < center_Y < (height/2) + 65:
                rov.yaw_left()
                rov.forward()
                return 0

            elif center_X > (width/2) + 65 and (height/2) - 65 < center_Y < (height/2) + 65:
                rov.yaw_right()
                rov.forward()
                return 0
            
            elif (width/2) - 65 < center_X < (width/2) + 65 and center_Y < (height/2) - 65:
                rov.pitch_up()
                rov.forward()
                return 0
            
            elif (width/2) - 65 < center_X < (width/2) + 65 and center_Y > (height/2) + 65:
                rov.pitch_down()
                rov.forward()
                return 0
        
            else:
                rov.forward()
                return 0               
    
    if h >= 310:         
        if h - 9 < w < h + 9:
            #araç çemberin tam ortasında
            rov.desired_direction()
            passing_count += 1
            return passing_count
            
        elif turn_right_indicator:
            rov.yaw_circular_right()
            return 0
            
        elif not turn_right_indicator:
            rov.yaw_circular_left()
            return 0
          

#yönlendirme komutlarının hızını kontrol etmek için  ve daireden geçerken komut kirlilqiğini önlemek için kullanılan sayaçlar
order_count = 0
passing_count = 0
# the folder path for the video
video_path = "Visual Studio Code\\Python\\Rov Videos\\front_2022-06-23_15_25_20 (2).avi"

if __name__ == "__main__":
    #Capturing the video and getting the dimensions of the camera to variables
    capture = cv2.VideoCapture(video_path)
    width = capture.get(3)
    height = capture.get(4)

    #Vehicle object
    rov = Rov()

    #video oynatma
    while True:
        success,frame = capture.read()
      
        
        if success:
            #Colour mask for red and yellow
            yellow_lower = np.array([0, 50, 0])
            yellow_upper = np.array([45, 255, 255])
            yellow_mask = cv2.inRange(frame,yellow_lower,yellow_upper)
            red_lower = np.array([0,0,150])
            red_upper = np.array([0,0,250])

            #Finding of the contours in the masked frame
            yellow_cnts,hierarchy = cv2.findContours(yellow_mask.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if len(yellow_cnts) > 0:
                #Finding the biggest contour are in yellow circle and drawing a rectangle around it
                yellow_area = max(yellow_cnts,key=cv2.contourArea)
                x,y,w,h = cv2.boundingRect(yellow_area)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,200),2)

                #Adjustments on the frame for distinguishing the rectangles
                red_mask = cv2.inRange(frame,red_lower,red_upper)
                blur = cv2.GaussianBlur(red_mask, (3,3), 0)
                thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
            
                #Filtering the frame
                red_cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                red_cnts = red_cnts[0] if len(red_cnts) == 2 else red_cnts[1]
                for red_c in red_cnts:
                    area = cv2.contourArea(red_c)
                    if area < 150:
                        cv2.drawContours(thresh, [red_c], -1, 0, -1)
        
                #karelerin köşelerini bulup resme çizdikten sonra kare sayısını bulma
                corners = cv2.goodFeaturesToTrack(thresh, 150, 0.5, 5)
                for corner in corners: 
                    x,y = corner.ravel()
                    cv2.circle(frame, (int(x),int(y)), 3, (36,255,12), -1)
                rectangle_count = len(corners)/4

            #Finding the center of the rectangle drawn around the circle
            (center_X,center_Y) = circle_center(x,y,w,h)

            # Finding where the center of the rectangle is located in reference to center of the camera
            if order_count == 0:
                if center_X > width / 2:
                    turn_right_indicator = 1
                    order_count += 1
            
                elif center_X < width / 2:
                    turn_right_indicator = 0
                    order_count += 1
        
            #movement_decider çıktısının verilmesi
            if order_count % 20 == 0:
                if passing_count >= 5:
                    if h < 310:
                        rov.stop()
                        order_count += 1
                
                    else:    
                        rov.desired_direction()
                        order_count += 1
                        
                else:
                    passing_count = movement_decider(x,y,w,h,width,height,turn_right_indicator,passing_count,rectangle_count)
                    order_count += 1
    
            else:
                order_count +=1
        
            cv2.imshow("frame",frame)

            
            if cv2.waitKey(7) == ord("q"):
                capture.release()
                cv2.destroyAllWindows()
                break
        
        else:
            print("Couldn't capture the video")
            break