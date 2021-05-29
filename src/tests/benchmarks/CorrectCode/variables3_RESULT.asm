.data
string1_1: .asciiz ""
string1_2: .asciiz "; "
string1_3: .asciiz "; "
string1_4: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -16
        sw      $fp, 16($sp)
        move    $fp, $sp
        lw      $8, 2($fp)
        li      $10, 10
        sw      $10, 4($fp)
        lw      $11, 2($fp)
        li      $13, 20
        sw      $13, 8($fp)
        lw      $14, 2($fp)
        li      $Error, 30
        sw      $Error, 12($fp)
        lw      $Error, 2($fp)
        lw      $Error, 2($fp)
        lw      $Error, 2($fp)
        la      $4, string1_1
        li      $v0, 4
        syscall 
                
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
                
        li      $v0, 1
        syscall 
        la      $4, string1_3
        li      $v0, 4
        syscall 
                
        li      $v0, 1
        syscall 
        la      $4, string1_4
        li      $v0, 4
        syscall 
        nop     
        move    $sp, $fp
        lw      $fp, 16($sp)
        addiu   $sp, $sp, 20
        li      $v0, 10
        syscall 