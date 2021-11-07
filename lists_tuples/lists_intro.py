computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)

# computer_parts[3] = "trackball"  # Change item at place number 3 # s[i] = x
print(computer_parts[3:])

computer_parts[3:] = ["trackball"]  # s[i:j] = t
print(computer_parts)

computer_parts[3:] = ()
print(computer_parts)