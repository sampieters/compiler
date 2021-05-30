.data
string1_1: .asciiz "Enter two numbers:\00"
string2_1: .asciiz ""
string2_2: .asciiz ""
string2_3: .asciiz "\00"
string3_1: .asciiz ""
string3_2: .asciiz "; "
string3_3: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -4
        sw      $fp, 4($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $8, 2($fp)
        addiu   $8, $fp, 2
        lw      $8, 3($fp)
        addiu   $8, $fp, 3
        la      $4, string2_1
        li      $v0, 5
        syscall 
        sw      $v0, LOCATION
                
        li      $v0, 1
        syscall 
        la      $4, string2_2
        li      $v0, 5
        syscall 
        sw      $v0, LOCATION
                
        li      $v0, 1
        syscall 
        la      $4, string2_3
        li      $v0, 5
        syscall 
        sw      $v0, LOCATION
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 2($fp)
        li      $v0, 1
        syscall 
        la      $4, string3_2
        li      $v0, 4
        syscall 
        lw      $4, 3($fp)
        li      $v0, 1
        syscall 
        la      $4, string3_3
        li      $v0, 4
        syscall 
        nop     
        move    $sp, $fp
        lw      $fp, 4($sp)
        addiu   $sp, $sp, 8
        li      $v0, 10
        syscall 