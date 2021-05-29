.data
string1_1: .asciiz ""
string1_2: .asciiz "\0A\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -16
        sw      $fp, 16($sp)
        move    $fp, $sp
        li      $8, 0
        sw      $8, 4($fp)
                
$L0:    
        # BEGIN WHILE CONDITION
        lw      $8, 4($fp)
        slti    $9, $8, 10
        beq     $9, $0, $L3
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
        # BEGIN IF CONDITION
        lw      $10, 4($fp)
        seq     $11, $10, 5
        beq     $11,$0, $L1
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        j       $L3
        # END IF BODY
        b       $L2
        nop     
$L1:    
        # BEGIN ELSE BODY
        lw      $12, 4($fp)
        addi    $13, $12, 1
                
        sw      $14, 8($fp)
        j       $L0
        # END ELSE BODY
$L2:    
        li      $24, 10
        sw      $24, 12($fp)
        j       $L0
        # END WHILE BODY
                
$L3:    
        nop     
        move    $sp, $fp
        lw      $fp, 16($sp)
        addiu   $sp, $sp, 20
        li      $v0, 10
        syscall 