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
        li      $9, 10
        sw      $9, 2($fp)
        lw      $9, 2($fp)
        li      $10, 20
        sw      $10, 24($fp)
        lw      $10, 2($fp)
        li      $11, 30
        sw      $11, 244($fp)
        lw      $11, 2($fp)
        lw      $12, 2($fp)
        lw      $13, 2($fp)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        sw      $11, 4($fp)
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        sw      $12, 8($fp)
        lw      $4, 8($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_3
        li      $v0, 4
        syscall 
        sw      $13, 12($fp)
        lw      $4, 12($fp)
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