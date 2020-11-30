#Program to renumber the excited states in a TALYS structure input file, so it doesn't go over the max number of excited states

def main():
  print("Hellooooo")

  input_file_name = "../../talys/structure/levels/final/Mg.lev"
  input_file = open(input_file_name,"r")
  output_file = open("Mg_shortened.lev","w")
  input_file_lines = input_file.readlines()

  mg_26_flag = 0
  over_60_flag = 0
  level_counter = 0
  for line in input_file_lines:
      token=line.split(" ")
      if any("27Mg" in s for s in token): #end of 26Mg section
          mg_26_flag = 0
          print("turned off")
          # print(token)

      if(mg_26_flag == 0):
          output_file.write(line)

      if(mg_26_flag == 1):
          # print(token)
          if(token[1] == token[2] == token[3] == '' and over_60_flag == 1):
              # print(token)
              print(line)
              output_file.write(line)


          if(token[1] == str(level_counter) or token[2] == str(level_counter) or token[3] == str(level_counter)):
              # print("level counter found")
              level_counter = level_counter + 1
              if(level_counter > 60):
                  over_60_flag = 1

                  if(token[2] !=''):
                      print("state greater than 60 and less than 100 found")
                      temp_int = int(token[2]) - 60
                      # token[2] = temp_int
                      # print(token)
                      value = line[2:4]
                      # print(value)
                      # print(int(value) - 60)

                      test_string = line[0:2] + str((int(value) - 60)) + line[4:]
                      output_file.write(test_string)
                      # print(line)


                  if(token[1] !=''):
                      print("state greater than 99 and less than 1000 found")
                      temp_int = int(token[1]) - 60
                      value = line[1:4]
                      # print(value)
                      # print(int(value) - 60)

                      test_string = line[0:1] + str((int(value) - 60)) + line[4:]
                      output_file.write(test_string)
                      # token[2] = temp_int
                      print(line)
                      # print(token[1])
                      # continue



      # print(line)
      # print(token)
      if any("26Mg" in s for s in token): #start of 26Mg section
          print("turned on")
          # print(token)
          mg_26_flag = 1

main()
