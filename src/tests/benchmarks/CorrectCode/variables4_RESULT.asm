.data
string1_1: .asciiz ""
string1_2: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -24
        sw      $fp, 20($sp)
        sw      $ra, 16($sp)
        sw      $4, 12($sp)
        move    $fp, $sp
        li      $8, 10
        sw      $8, 0($fp)
        addiu   $8, $fp, 0
        sw      $8, 4($fp)
        lw      $8, 4($fp)
        la      $4, string1_1
        li      $2, 4
        syscall 
        lw      $4, 4($fp)
        lw      $4, 0($4)
        li      $2, 1
        syscall 
        la      $4, string1_2
        li      $2, 4
        syscall 
        li      $v0, 0
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 12($sp)
        lw      $ra, 16($sp)
        lw      $fp, 20($sp)
        addiu   $sp, $sp, 24
        li      $2, 10
        syscall 