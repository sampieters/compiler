.data
string1_1: .asciiz ""
string1_2: .asciiz "; "
string1_3: .asciiz "; "
string1_4: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -12
        sw      $fp, 12($sp)
        move    $fp, $sp
        li      $8, 10
        sw      $8, 4($fp)
        lw      $8, 4($fp)
        sw      $8, 3($fp)
        lw      $8, 3($fp)
        sw      $8, 8($fp)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, 3($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        lw      $4, 3($fp)
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
        nop     
        move    $sp, $fp
        lw      $fp, 12($sp)
        addiu   $sp, $sp, 16
        li      $v0, 10
        syscall 