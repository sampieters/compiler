.data
string1_1: .asciiz "Enter a 5-character string:\00"
string2_1: .asciiz "%5s\00"
string3_1: .asciiz ""
string3_2: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -12
        sw      $fp, 12($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $8, 2($fp)
        addiu   $8, $fp, 2
        la      $4, string2_1
        li      $v0, 5
        syscall 
        sw      $v0, LOCATION
        sw      $8, 8($fp)
        lw      $4, 8($fp)
        li      $v0, None
        syscall 
        la      $4, string2_2
        li      $v0, 5
        syscall 
        sw      $v0, LOCATION
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 2($fp)
        li      $v0, None
        syscall 
        la      $4, string3_2
        li      $v0, 4
        syscall 
        nop     
        move    $sp, $fp
        lw      $fp, 12($sp)
        addiu   $sp, $sp, 16
        li      $v0, 10
        syscall 