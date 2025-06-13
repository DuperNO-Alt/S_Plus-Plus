; Test Program for testing and understanding the changes the language made

segment .text
    global _start

_start:
    mov ax, 255
    mov ax, bx

    cmp ax, bx
    je test
    cmp ax, cx
    ja test2
    jmp test

test:
    mov cx, 255

test2:
    ret