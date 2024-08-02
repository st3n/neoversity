; nasm -f bin -o test.com task-1.asm 

org  0x100               ; Вказуємо, що це програма .COM
section .data
    a db 2               
    b db 1               
    c db 4              
    resultMsg db 'Result: $' ; Визначення рядка для виведення результату

; b - c + a
section .text
_start:

    ;mov ebx, 9
    ;push ebx
    ;mov ebx, 0

    ;reg = b
    ;reg += c
    ;reg -= a


    mov al, b ; Копіюємо значення адреси b (для прикладу 0x1356) у регістр al          
    add al, [c] ; Додаємо значення по адресі [с] у регістр al та збергігаємо результат в al 
    sub al, [a] ; Віднімаємо значення по адресі [a] у регістр al та збергігаємо результат в al 

    ;pop ebx
    ;mov al, bl
    ;inc al
    ;imul eax, ebx, 3

    ; Перетворення результату в ASCII символ (для однозначних чисел)
    add al, 30h          ; Перетворюємо число в ASCII символ
    ; 30h is the ASCII code for a digit '0'. 
    ; 31h, 32h, ... 39h correspond to '1', '2',... '9'
    ; 41h is the ASCII code for a letter 'A'.

    ; Вивід результату
    mov ah, 09h          ; Функція DOS для виводу рядка
    lea dx, resultMsg    ; Встановлюємо DX на адресу resultMsg
    int 21h              ; Виклик DOS-переривання

    ; Вивід числа
    mov dl, al           ; Поміщаємо результат в dl для виводу
    mov ah, 02h          ; Функція DOS для виводу символу
    int 21h              ; Виклик DOS-переривання

    ; Завершення програми
    mov ax, 4c00h        ; Функція DOS для завершення програми
    int 21h              ; Виклик DOS-переривання
