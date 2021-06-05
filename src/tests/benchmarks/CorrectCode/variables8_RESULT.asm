.data
string1_1: .asciiz ""
string1_2: .asciiz "; \00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -32
        sw      $fp, 28($sp)
        sw      $ra, 24($sp)
        sw      $4, 20($sp)
        move    $fp, $sp
        li      $9, 10
        sw      $9, 0($fp)
        li      $10, 20
        sw      $10, 4($fp)
        li      $11, 30
        sw      $11, 8($fp)
        li      $11, 1
        sw      $11, 12($fp)
                
$L0:    
        # BEGIN WHILE CONDITION
        lw      $11, 12($fp)
        slti    $11, $11, 4
        sw      $11, 16($fp)
        lw      $11, 16($fp)
        beq     $11, $0, $L1
        nop     
        # END WHILE CONDITION
                
        # BEGIN WHILE BODY
        lw      $11, 12($fp)
        subi    $11, $11, 1
        sll     $11, $11, 2
        add     $11, $11, 0
        add     $11, $11, $fp
        la      $4, string1_1
        li      $2, 4
        syscall 
        lw      $4, 0($11)
        li      $2, 1
        syscall 
        la      $4, string1_2
        li      $2, 4
        syscall 
        lw      $12, 12($fp)
        addiu   $12, $12, 1
        sw      $12, 12($fp)
        j       $L0
        # END WHILE BODY
                
$L1:    
        li      $v0, 1
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 20($sp)
        lw      $ra, 24($sp)
        lw      $fp, 28($sp)
        addiu   $sp, $sp, 32
        li      $2, 10
        syscall 