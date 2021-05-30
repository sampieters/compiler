.data
string1_1: .asciiz ""
string1_2: .asciiz "; "
string1_3: .asciiz "; "
string1_4: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -24
        sw      $fp, 20($sp)
        sw      $ra, 16($sp)
        sw      $4, 12($sp)
        move    $fp, $sp
        li      $9, 10
        sw      $9, 0($fp)
        li      $10, 20
        sw      $10, 4($fp)
        li      $11, 30
        sw      $11, 8($fp)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, 0($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_3
        li      $v0, 4
        syscall 
        lw      $4, 8($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_4
        li      $v0, 4
        syscall 
        move    $sp, $fp
        lw      $4, 12($sp)
        lw      $ra, 16($sp)
        lw      $fp, 20($sp)
        addiu   $sp, $sp, 24
        li      $v0, 10
        syscall 