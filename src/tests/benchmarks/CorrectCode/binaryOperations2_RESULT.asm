.data
string1: .asciiz "%d; \00"
string2: .asciiz "%d; \00"
string3: .asciiz "%d; \00"
string4: .asciiz "%d; \00"
.globl main
.text
                
main:   
        addiu   $sp,$sp, -4
        sw      $fp,4($sp)
        move    $fp,$sp
        la      $4,string1
        li      $v0,4
        syscall 
        li      $4,10
        li      $v0,1
        syscall 
        la      $4,string2
        li      $v0,4
        syscall 
        li      $4,10
        li      $v0,1
        syscall 
        la      $4,string3
        li      $v0,4
        syscall 
        li      $4,10
        li      $v0,1
        syscall 
        la      $4,string4
        li      $v0,4
        syscall 
        li      $4,10
        li      $v0,1
        syscall 
        nop     
        move    $sp,$fp
        lw      $fp,4($sp)
        addiu   $sp,$sp,8
        li      $v0,10
        syscall 