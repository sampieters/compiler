.data
string1_1: .asciiz ""
string1_2: .asciiz "\0A\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -12
        sw      $fp, 12($sp)
        move    $fp, $sp
        li      $8, 0
        sw      $8, 4($fp)
                
$L0:    
        # BEGIN WHILE CONDITION
        lw      $8, 4($fp)
        slti    $9, $8, 10
        beq     $9, $0, $L1
        nop     
        # END WHILE CONDITION
                
        # BEGIN WHILE BODY
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        lw      $10, 4($fp)
        addi    $11, $10, 1
                
        sw      $12, 8($fp)
        j       $L0
        # END WHILE BODY
                
$L1:    
        nop     
        move    $sp, $fp
        lw      $fp, 12($sp)
        addiu   $sp, $sp, 16
        li      $v0, 10
        syscall 