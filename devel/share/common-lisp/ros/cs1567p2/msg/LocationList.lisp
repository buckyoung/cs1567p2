; Auto-generated. Do not edit!


(cl:in-package cs1567p2-msg)


;//! \htmlinclude LocationList.msg.html

(cl:defclass <LocationList> (roslisp-msg-protocol:ros-message)
  ((robots
    :reader robots
    :initarg :robots
    :type (cl:vector cs1567p2-msg:Location)
   :initform (cl:make-array 0 :element-type 'cs1567p2-msg:Location :initial-element (cl:make-instance 'cs1567p2-msg:Location))))
)

(cl:defclass LocationList (<LocationList>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LocationList>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LocationList)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cs1567p2-msg:<LocationList> is deprecated: use cs1567p2-msg:LocationList instead.")))

(cl:ensure-generic-function 'robots-val :lambda-list '(m))
(cl:defmethod robots-val ((m <LocationList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cs1567p2-msg:robots-val is deprecated.  Use cs1567p2-msg:robots instead.")
  (robots m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LocationList>) ostream)
  "Serializes a message object of type '<LocationList>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'robots))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'robots))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LocationList>) istream)
  "Deserializes a message object of type '<LocationList>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'robots) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'robots)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'cs1567p2-msg:Location))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LocationList>)))
  "Returns string type for a message object of type '<LocationList>"
  "cs1567p2/LocationList")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LocationList)))
  "Returns string type for a message object of type 'LocationList"
  "cs1567p2/LocationList")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LocationList>)))
  "Returns md5sum for a message object of type '<LocationList>"
  "d5407510fcfc38766911870496eed14d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LocationList)))
  "Returns md5sum for a message object of type 'LocationList"
  "d5407510fcfc38766911870496eed14d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LocationList>)))
  "Returns full string definition for message of type '<LocationList>"
  (cl:format cl:nil "Location[] robots~%~%================================================================================~%MSG: cs1567p2/Location~%int32 robot_num~%float32 x~%float32 y~%float32 theta~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LocationList)))
  "Returns full string definition for message of type 'LocationList"
  (cl:format cl:nil "Location[] robots~%~%================================================================================~%MSG: cs1567p2/Location~%int32 robot_num~%float32 x~%float32 y~%float32 theta~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LocationList>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'robots) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LocationList>))
  "Converts a ROS message object to a list"
  (cl:list 'LocationList
    (cl:cons ':robots (robots msg))
))
