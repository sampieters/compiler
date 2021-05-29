.data
string1_1: .asciiz ""
string1_2: .asciiz "\0A\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -8
        sw      $fp, 8($sp)
        move    $fp, $sp
        li      $8, 0
        sw      $8, 4($fp)
                
$L0:    
        # BEGIN WHILE CONDITION
        lw      $9, 0($fp)
        slti    $10, $9, 10
        beq     $10, $0, $L1
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
        lw      $11, 0($fp)
        addiu   $12, $12, 1
        j       $L0
        # END WHILE BODY
                
$L1:    
        nop     
        move    $sp, $fp
        lw      $fp, 8($sp)
        addiu   $sp, $sp, 12
        li      $v0, 10
        syscall 