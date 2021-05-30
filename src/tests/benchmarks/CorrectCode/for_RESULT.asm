.data
string1_1: .asciiz ""
string1_2: .asciiz "\n\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -32
        sw      $fp, 28($sp)
        sw      $ra, 24($sp)
        sw      $4, 20($sp)
        move    $fp, $sp
        li      $8, 0
        sw      $8, 0($fp)
                
$L0:    
        # BEGIN WHILE CONDITION
        lw      $8, 0($fp)
        slti    $8, $8, 10
        sw      $8, 4($fp)
        lw      $8, 4($fp)
        beq     $8, $0, $L1
        nop     
        # END WHILE CONDITION
                
        # BEGIN WHILE BODY
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, 0($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        lw      $8, 0($fp)
        addi    $8, $8, 1
        sw      $8, 8($fp)
        lw      $8, 8($fp)
        sw      $8, 12($fp)
        lw      $8, 12($fp)
        sw      $8, 16($fp)
        j       $L0
        # END WHILE BODY
                
$L1:    
        move    $sp, $fp
        lw      $4, 20($sp)
        lw      $ra, 24($sp)
        lw      $fp, 28($sp)
        addiu   $sp, $sp, 32
        li      $v0, 10
        syscall 