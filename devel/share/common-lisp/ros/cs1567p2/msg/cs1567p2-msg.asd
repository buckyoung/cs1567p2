
(cl:in-package :asdf)

(defsystem "cs1567p2-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Location" :depends-on ("_package_Location"))
    (:file "_package_Location" :depends-on ("_package"))
    (:file "LocationList" :depends-on ("_package_LocationList"))
    (:file "_package_LocationList" :depends-on ("_package"))
  ))