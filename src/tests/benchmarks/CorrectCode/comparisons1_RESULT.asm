.data
string1: .asciiz "%d; \00"
string2: .asciiz "%d; \00"
string3: .asciiz "%d; \00"
string4: .asciiz "%d; \00"
string5: .asciiz "%d; \00"
string6: .asciiz "%d; \00"
.globl main
.text
                
main:   
        addiu   $sp,$sp, -4
        sw      $fp,4($sp)
        move    $fp,$sp
        la      $6,string1
        li      $6,1
        li      $6,1
        li      $v0,1
        syscall 
        la      $6,string2
        li      $6,0
        li      $6,0
        li      $v0,1
        syscall 
        la      $6,string3
        li      $6,1
        li      $6,1
        li      $v0,1
        syscall 
        la      $6,string4
        li      $6,0
        li      $6,0
        li      $v0,1
        syscall 
        la      $6,string5
        li      $6,1
        li      $6,1
        li      $v0,1
        syscall 
        la      $6,string6
        li      $6,0
        li      $6,0
        li      $v0,1
        syscall 
        nop     
        move    $sp,$fp
        lw      $fp,4($sp)
        addiu   $sp,$sp,8
        li      $v0,10
        syscall 