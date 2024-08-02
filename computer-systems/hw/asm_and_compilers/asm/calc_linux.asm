section .data
    a db 5               ; Define a = 5
    b db 3               ; Define b = 3
    c db 2               ; Define c = 2
    resultMsg db 'Result: ', 0

section .bss
    result resb 2        ; Reserve a byte for the result

section .text
    global _start

_start:
    ; Perform the arithmetic operation
    mov al, [b]          ; Load a into al
    sub al, [c]          ; Add b to al
    add al, [a]          ; Subtract c from al

    ; Convert result to ASCII
    add al, '0'          ; Convert the result to ASCII

    ; Store the result
    mov [result], al
    mov byte [result+1], 0x0A  ; Append newline character

    ; Write the resultMsg
    mov rax, 1           ; syscall number for sys_write
    mov rdi, 1           ; file descriptor 1 is stdout
    lea rsi, [resultMsg] ; pointer to the resultMsg
    mov rdx, 8           ; length of the message
    syscall              ; call kernel

    ; Write to stdout
    mov rax, 1           ; syscall number for sys_write
    mov rdi, 1           ; file descriptor 1 is stdout
    lea rsi, [result]    ; pointer to the result
    mov rdx, 2           ; length of the result
    syscall              ; call kernel

    ; Exit the program
    mov rax, 60          ; syscall number for sys_exit
    xor rdi, rdi         ; exit code 0
    syscall              ; call kernel

