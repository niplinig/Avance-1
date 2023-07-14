# Algoritmo 1

def insertion_sort(array_datos)
    for i in 1...(array_datos.length)  # Step 1
        j = i # Step 2
        while j > 0 # Step 3
            if array_datos[j-1] > array_datos[j] # Step 4
                temp = array_datos[j]
                array_datos[j] = array_datos[j-1]
                array_datos[j-1] = temp
            else
                break
            end
            j = j - 1 # Step 5
        end
    end
    return array_datos
end

# Algoritmo 2

def merge(array_datos, sorted_left, sorted_right)
  left_size = sorted_left.length
  right_size = sorted_right.length
  array_pointer = 0
  left_pointer = 0
  right_pointer = 0
  while left_pointer < left_size && right_pointer < right_size
    if sorted_left[left_pointer] < sorted_right[right_pointer]
      array_datos[array_pointer] = sorted_left[left_pointer]
      left_pointer+=1
    else
      array_datos[array_pointer] = sorted_right[right_pointer]
      right_pointer+=1
    end
    array_pointer+=1
  end
  while left_pointer < left_size
      array_datos[array_pointer] = sorted_left[left_pointer]
      left_pointer+=1
      array_pointer+=1
  end
  while right_pointer < right_size
     array_datos[array_pointer] = sorted_right[right_pointer]
     right_pointer+=1
     array_pointer+=1
  end
  return array_datos
end

# Algoritmo 3

nombre= 'Xavier'
Apellido= "Pauta"
numeros= [1,2,3,4 ,5 ]
datos= { "Nombre"=>'Xavier Pauta' , edad: 21}

student1 = {
  name: "Juan",
  grades: {
    "Matemáticas" => 95,
    "Ciencias" => 87,
    "Historia" => 92,
    "Inglés" => 88
  }
}

edad= 23
case edad
when 10
    puts 'a'
when 15
    puts 'b'
else
    puts 'c'
end

