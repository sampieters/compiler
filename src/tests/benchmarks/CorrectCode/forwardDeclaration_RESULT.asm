.data
string1: .asciiz "Hello \00"
string2: .asciiz "World\0A\00"
string3: .asciiz "World\0A\00"
.globl main
.text
                
f:      
        addiu   $sp,$sp, -4
        sw      $fp,4($sp)
        move    $fp,$sp
        la      $6,string1
        nop     
        move    $sp,$fp
        lw      $fp,4($sp)
        addiu   $sp,$sp,8
        jr      $ra
                
g:      
        addiu   $sp,$sp, -12
        sw      $fp,12($sp)
        move    $fp,$sp
        la      $6,string2
        jal     f
        la      $6,string3
        nop     
        move    $sp,$fp
        lw      $fp,12($sp)
        addiu   $sp,$sp,16
        jr      $ra
                
main:   
        addiu   $sp,$sp, -20
        sw      $fp,20($sp)
        move    $fp,$sp
        jal     f
        jal     g
        nop     
        move    $sp,$fp
        lw      $fp,20($sp)
        addiu   $sp,$sp,24
        li      $v0,10
        syscall 